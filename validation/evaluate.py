import requests
import json
import time
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000"

# =========================================
# TEST CASES
# =========================================

TEST_CASES = [

    # ── Original 5 tests ──────────────────

    {
        "id": "TC001",
        "category": "Needs Assessment",
        "query": "I am 32 diabetic suggest insurance",
        "expected_keywords": ["Diabetes-friendly Health Insurance", "Term Life Insurance"]
    },
    {
        "id": "TC002",
        "category": "Policy Comparison",
        "query": "Compare health insurance plans",
        "expected_keywords": ["HDFC Ergo", "Niva Bupa"]
    },
    {
        "id": "TC003",
        "category": "Premium Estimation",
        "query": "Estimate premium for 1Cr coverage age 45 smoker diabetic",
        "expected_keywords": ["21840"]
    },
    {
        "id": "TC004",
        "category": "Needs Assessment",
        "query": "I am married with 2 children earning 20L",
        "expected_keywords": ["Family Health Insurance", "Critical Illness Rider"]
    },
    {
        "id": "TC005",
        "category": "Needs Assessment – Edge Case",
        "query": "I am a cancer patient with 10 dependents",
        "expected_keywords": ["Critical Illness Insurance", "Group Insurance Plan"]
    },

    # ── New tests: Needs Assessment ───────

    {
        "id": "TC006",
        "category": "Needs Assessment",
        "query": "I am 25 years old software engineer with no health issues, what insurance should I buy?",
        "expected_keywords": ["Term Life Insurance", "Health Insurance"]
    },
    {
        "id": "TC007",
        "category": "Needs Assessment",
        "query": "I am 55 years old retired with no existing coverage",
        "expected_keywords": ["Senior Citizen Health Insurance", "Critical Illness"]
    },
    {
        "id": "TC008",
        "category": "Needs Assessment",
        "query": "I am a 40 year old self-employed person with 3 dependents and no insurance",
        "expected_keywords": ["Family Health Insurance", "Term Life Insurance"]
    },
    {
        "id": "TC009",
        "category": "Needs Assessment",
        "query": "I am 28 years old newly married no dependents earning 8 LPA",
        "expected_keywords": ["Health Insurance", "Term Life Insurance"]
    },
    {
        "id": "TC010",
        "category": "Needs Assessment – Edge Case",
        "query": "I am 70 years old with heart disease and diabetes",
        "expected_keywords": ["Senior Citizen Health Insurance", "Critical Illness"]
    },

    # ── New tests: Premium Estimation ─────

    {
        "id": "TC011",
        "category": "Premium Estimation",
        "query": "Estimate premium for 50 lakh coverage for a 30 year old non-smoker",
        "expected_keywords": ["premium", "annual", "monthly"]
    },
    {
        "id": "TC012",
        "category": "Premium Estimation",
        "query": "What will be my yearly premium for 2 crore term insurance at age 35?",
        "expected_keywords": ["yearly_premium", "premium"]
    },
    {
        "id": "TC013",
        "category": "Premium Estimation",
        "query": "Calculate premium for 25 lakh coverage for a 50 year old smoker",
        "expected_keywords": ["premium", "smoker"]
    },
    {
        "id": "TC014",
        "category": "Premium Estimation",
        "query": "How much will I pay monthly for 75 lakh coverage at age 42?",
        "expected_keywords": ["monthly_premium", "premium"]
    },

    # ── New tests: Policy Comparison ──────

    {
        "id": "TC015",
        "category": "Policy Comparison",
        "query": "Compare term life insurance policies available",
        "expected_keywords": ["Term Life", "premium", "coverage"]
    },
    {
        "id": "TC016",
        "category": "Policy Comparison",
        "query": "Which health insurance has the best claim settlement ratio?",
        "expected_keywords": ["claim", "ratio", "HDFC"]
    },
    {
        "id": "TC017",
        "category": "Policy Comparison",
        "query": "Compare Star Health vs Niva Bupa health insurance",
        "expected_keywords": ["Star Health", "Niva Bupa"]
    },
    {
        "id": "TC018",
        "category": "Policy Comparison",
        "query": "Show me health plans with coverage above 15 lakh",
        "expected_keywords": ["coverage", "premium", "health"]
    },

    # ── New tests: Coverage Gap Detection ─

    {
        "id": "TC019",
        "category": "Coverage Gap",
        "query": "I have a basic employer health insurance of 3 lakhs, am I adequately covered?",
        "expected_keywords": ["coverage_gap", "inadequate", "top-up"]
    },
    {
        "id": "TC020",
        "category": "Coverage Gap",
        "query": "I only have term insurance but no health coverage, what am I missing?",
        "expected_keywords": ["Health Insurance", "coverage_gap"]
    },
    {
        "id": "TC021",
        "category": "Coverage Gap",
        "query": "I have health insurance but no life cover, I have 2 kids",
        "expected_keywords": ["Term Life Insurance", "coverage_gap"]
    },

    # ── New tests: Edge Cases & Robustness ─

    {
        "id": "TC022",
        "category": "Edge Case – Minimal Input",
        "query": "insurance",
        "expected_keywords": ["insurance", "health", "policy"]
    },
    {
        "id": "TC023",
        "category": "Edge Case – Ambiguous",
        "query": "I need something for my family",
        "expected_keywords": ["Family Health Insurance", "Term Life"]
    },
    {
        "id": "TC024",
        "category": "Edge Case – Out of Scope",
        "query": "What is the weather today?",
        "expected_keywords": ["insurance", "help"]
    },
    {
        "id": "TC025",
        "category": "Edge Case – Multilingual / Informal",
        "query": "Mujhe insurance chahiye, main 35 saal ka hoon",
        "expected_keywords": ["insurance", "health", "term"]
    },

    # ── New tests: Multi-turn Context ─────

    {
        "id": "TC026",
        "category": "Multi-turn – Follow Up",
        "query": "Tell me more about the first recommendation you gave",
        "expected_keywords": ["insurance", "policy", "coverage"]
    },
    {
        "id": "TC027",
        "category": "Multi-turn – Clarification",
        "query": "What does claim settlement ratio mean?",
        "expected_keywords": ["claim settlement", "ratio", "percentage"]
    },
    {
        "id": "TC028",
        "category": "Multi-turn – Refinement",
        "query": "Can you suggest something cheaper than what you recommended?",
        "expected_keywords": ["premium", "affordable", "plan"]
    },

    # ── New tests: Specific Conditions ────

    {
        "id": "TC029",
        "category": "Medical Condition",
        "query": "I have hypertension and asthma, which insurers will cover me?",
        "expected_keywords": ["Health Insurance", "pre-existing", "coverage"]
    },
    {
        "id": "TC030",
        "category": "Medical Condition",
        "query": "I am a 38 year old with kidney disease, suggest suitable policies",
        "expected_keywords": ["Critical Illness", "Health Insurance"]
    },
]


# =========================================
# RUNNER
# =========================================

def reset_session():
    try:
        requests.post(f"{BASE_URL}/reset", timeout=5)
    except Exception:
        pass


def run_test(tc: dict) -> dict:
    reset_session()
    time.sleep(0.3)

    start = time.time()

    try:
        resp = requests.post(
            f"{BASE_URL}/chat",
            json={"message": tc["query"]},
            timeout=60
        )
        resp.raise_for_status()
        data = resp.json()
        elapsed = round(time.time() - start, 2)

        assistant = data.get("assistant_response", {})

        # Flatten all text fields for keyword search
        full_text = json.dumps(assistant).lower()

        matched   = [kw for kw in tc["expected_keywords"] if kw.lower() in full_text]
        missed    = [kw for kw in tc["expected_keywords"] if kw.lower() not in full_text]

        passed    = len(missed) == 0
        score     = round(len(matched) / len(tc["expected_keywords"]) * 100, 1)

        return {
            "id":               tc["id"],
            "category":         tc["category"],
            "query":            tc["query"],
            "status":           "PASS" if passed else "PARTIAL" if matched else "FAIL",
            "score":            score,
            "matched":          matched,
            "missed":           missed,
            "response_time_s":  elapsed,
            "raw_summary":      assistant.get("summary", "")[:200],
        }

    except requests.exceptions.ConnectionError:
        return {
            "id": tc["id"], "category": tc["category"], "query": tc["query"],
            "status": "ERROR", "score": 0, "matched": [], "missed": tc["expected_keywords"],
            "response_time_s": 0, "raw_summary": "Backend not reachable",
        }
    except Exception as e:
        return {
            "id": tc["id"], "category": tc["category"], "query": tc["query"],
            "status": "ERROR", "score": 0, "matched": [], "missed": tc["expected_keywords"],
            "response_time_s": 0, "raw_summary": str(e),
        }


# =========================================
# REPORT PRINTER
# =========================================

def print_report(results: list):
    total   = len(results)
    passed  = sum(1 for r in results if r["status"] == "PASS")
    partial = sum(1 for r in results if r["status"] == "PARTIAL")
    failed  = sum(1 for r in results if r["status"] in ("FAIL", "ERROR"))
    avg_score = round(sum(r["score"] for r in results) / total, 1)
    avg_time  = round(sum(r["response_time_s"] for r in results) / total, 2)

    sep = "=" * 80

    print(f"\n{sep}")
    print(f"  INSURANCE BOT EVALUATION REPORT  —  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(sep)
    print(f"  Total Tests : {total}")
    print(f"  PASS        : {passed}  ({round(passed/total*100)}%)")
    print(f"  PARTIAL     : {partial}")
    print(f"  FAIL/ERROR  : {failed}")
    print(f"  Avg Score   : {avg_score}%")
    print(f"  Avg Latency : {avg_time}s")
    print(sep)

    # Group by category
    categories = {}
    for r in results:
        categories.setdefault(r["category"], []).append(r)

    for cat, items in categories.items():
        cat_pass = sum(1 for i in items if i["status"] == "PASS")
        print(f"\n  [{cat}]  {cat_pass}/{len(items)} passed")
        for r in items:
            icon = "✅" if r["status"] == "PASS" else "⚠️" if r["status"] == "PARTIAL" else "❌"
            print(f"    {icon} {r['id']}  score={r['score']}%  time={r['response_time_s']}s")
            print(f"       Q: {r['query'][:70]}")
            if r["missed"]:
                print(f"       MISSED: {r['missed']}")
            if r["raw_summary"]:
                print(f"       SUMMARY: {r['raw_summary'][:120]}...")

    print(f"\n{sep}\n")


# =========================================
# SAVE JSON REPORT
# =========================================

def save_json_report(results: list, path: str = "eval_report.json"):
    report = {
        "timestamp": datetime.now().isoformat(),
        "summary": {
            "total":   len(results),
            "passed":  sum(1 for r in results if r["status"] == "PASS"),
            "partial": sum(1 for r in results if r["status"] == "PARTIAL"),
            "failed":  sum(1 for r in results if r["status"] in ("FAIL", "ERROR")),
            "avg_score_pct": round(sum(r["score"] for r in results) / len(results), 1),
            "avg_latency_s": round(sum(r["response_time_s"] for r in results) / len(results), 2),
        },
        "results": results,
    }
    with open(path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"  JSON report saved → {path}")


# =========================================
# MAIN
# =========================================

if __name__ == "__main__":
    print(f"\nRunning {len(TEST_CASES)} tests against {BASE_URL} ...\n")

    results = []
    for tc in TEST_CASES:
        print(f"  Running {tc['id']} — {tc['query'][:55]}...")
        result = run_test(tc)
        results.append(result)

    print_report(results)
    save_json_report(results, "eval_report.json")