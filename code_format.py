import autopep8
import jsbeautifier
import shortuuid

def format_code(code,language):
    file_id = str(shortuuid.ShortUUID().random(length=7))
    if language=="python":
        formatted_code = autopep8.fix_code(code)

        with open(f"{file_id}.py", "w") as f:
            f.write(formatted_code)

        return f"Formatted Python code has been written to {file_id}.py."
    elif language=="javascript":
        options = jsbeautifier.default_options()
        formatted_code = jsbeautifier.beautify(code, options)

        with open(f"{file_id}.js", "w") as f:
            f.write(formatted_code)

        return f"Formatted JavaScript code has been written to {file_id}.js."
    else:
        return "Language is not supported"
