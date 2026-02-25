# Epic Title: Test Portal Usability on Various Screen Sizes

import json
from datetime import datetime

class TestReportGenerator:

    def __init__(self):
        self.reports = []

    def log_report(self, scenario: str, result: bool, issues: list):
        self.reports.append({
            "scenario": scenario,
            "result": "Pass" if result else "Fail",
            "issues": issues,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    def generate_report(self, file_path: str):
        with open(file_path, 'w') as file:
            json.dump(self.reports, file, indent=4)

    def clear_reports(self):
        self.reports = []