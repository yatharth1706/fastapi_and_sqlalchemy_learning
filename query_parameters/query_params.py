from fastapi import APIRouter

router = APIRouter()


@router.get("/calculate_two_numbers")
def calculate_sum(a:int = 0, b:int | None = 0):
    return {"result": a+b}

@router.get("/mix_path_and_query_params/path/{path_name}")
def path_with_params(path_name: str, q: str | None = None):
    return {
        "path_name": path_name,
        "query": q

    }