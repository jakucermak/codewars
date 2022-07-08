def solution(s: str):
    result = ""
    '''
    for i in s:
        if i.isupper():
            result += f" {i}"
        else:
            result += i
    '''
    return result.join([f" {c}" if c.isupper() else c for c in s])

def test_camel():
    assert solution("helloWorld") == "hello World"
    assert solution("camelCase") == "camel Case"
    assert solution("breakCamelCase") == "break Camel Case"


