from flask import Flask, request, jsonify
from crew import Reseach_crew  # Make sure this file defines your crew correctly
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

@app.route('/research', methods=['POST'])
def run_crew():
    data = request.get_json()

    # Check if topic is provided
    if not data or 'topic' not in data:
        return jsonify({'error': "Missing 'topic' in request"}), 400

    topic = data['topic']
    date = datetime.now().strftime("%Y-%m-%d")

    inputs = {
        'topic': topic,
        'date': date
    }

    try:
        # Run the Crew and generate the report
        Reseach_crew().crew().kickoff(inputs=inputs)

        # Read the generated markdown report
        report_path = Path("report.md")
        if report_path.exists():
            report_content = report_path.read_text(encoding='utf-8')
        else:
            report_content = "⚠️ Report file not found."

        # Return only simple, JSON-serializable data
        return jsonify({
            'topic': topic,
            'report': report_content
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
