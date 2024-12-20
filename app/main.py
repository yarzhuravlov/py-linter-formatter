flake8_error_prop_to_inner_prop = {
    "code": "name",
    "line_number": "line",
    "column_number": "column",
    "text": "message",
    "source": "source"
}


def format_linter_error(error: dict) -> dict:
    return {
        flake8_error_prop_to_inner_prop[flake_prop]: value
        for (flake_prop, value) in [*error.items(), ("source", "flake8")]
        if flake_prop in flake8_error_prop_to_inner_prop.keys()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": [
            format_linter_error(error) for error in errors
        ],
        "path": file_path,
        "status": "passed" if len(errors) == 0 else "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        format_single_linter_file(file_path=file_path, errors=errors_in_file)
        for file_path, errors_in_file in linter_report.items()
    ]
