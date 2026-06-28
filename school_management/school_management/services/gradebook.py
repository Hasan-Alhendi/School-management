import json


def _as_list(value):
    if not value:
        return []
    if isinstance(value, str):
        return json.loads(value)
    return value


def calculate_term_result(scores, scheme=None):
    """Calculate a term result from flexible assessment components.

    scores example:
    [
      {"category": "Works", "score": 50},
      {"category": "Exam", "score": 100}
    ]
    """
    rows = _as_list(scores)
    work_score = sum(float(row.get("score") or 0) for row in rows if row.get("category") in ["Works", "أعمال"])
    exam_score = sum(float(row.get("score") or 0) for row in rows if row.get("category") in ["Exam", "امتحان"])

    formula = None
    if isinstance(scheme, dict):
        formula = scheme.get("final_formula")
    elif isinstance(scheme, str) and scheme:
        try:
            formula = json.loads(scheme).get("final_formula")
        except Exception:
            formula = scheme

    if formula == "WORK_PLUS_EXAM_NO_DIVISION":
        term_total = work_score + exam_score
    else:
        term_total = (work_score + exam_score) / 2

    return {
        "work_score": work_score,
        "exam_score": exam_score,
        "term_total": term_total,
    }
