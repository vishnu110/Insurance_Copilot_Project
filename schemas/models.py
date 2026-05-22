from typing import List, Dict, Any
from pydantic import BaseModel


class InsuranceResponse(BaseModel):

    response_type: str

    recommendations: List[str]

    coverage_gaps: List[str]

    premium_details: Dict[str, Any]

    policy_comparisons: List[Dict[str, Any]]

    summary: str