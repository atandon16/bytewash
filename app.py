import os
import pandas as pd
from flask import Flask, render_template, request, send_file
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Process data
            df = pd.read_excel(filepath) if file.filename.endswith(".xlsx") else pd.read_csv(filepath)

            total_rows = len(df)
            duplicate_count = df.duplicated().sum()
            missing_counts = df.isnull().sum().to_dict()

            # Example cleaning
            cleaned_df = df.drop_duplicates()
            cleaned_df = cleaned_df.applymap(lambda x: x.title() if isinstance(x, str) else x)

            # Save cleaned preview
            cleaned_filepath = os.path.join(REPORT_FOLDER, f"cleaned_{file.filename}")
            cleaned_df.to_csv(cleaned_filepath, index=False)

            # Generate HTML report
            report_html = render_template(
                "report.html",
                total_rows=total_rows,
                duplicate_count=duplicate_count,
                missing_counts=missing_counts,
                cleaned_sample=cleaned_df.head().to_html(classes='table table-bordered', index=False)
            )

            report_path = os.path.join(REPORT_FOLDER, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(report_html)

            return send_file(report_path, as_attachment=True)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)