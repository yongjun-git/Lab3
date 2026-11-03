import employee_info
import pytest

def test_get_employees_by_age_range():
    result = employee_info.get_employees_by_age_range(30, 40)
    assert len(result) == 2
    assert result[0]["name"] == "Chloe"
    assert result[1]["name"] == "Mike"

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert result == pytest.approx(361000 / 6)

def test_get_employees_by_dept():
    result = employee_info.get_employees_by_dept("Engineering")
    assert len(result) == 2
    assert result[0]["name"] == "Chloe"
    assert result[1]["name"] == "Mike"

def test_get_employees_by_dept_not_found():
    result = employee_info.get_employees_by_dept("HR")
    assert result == []
    