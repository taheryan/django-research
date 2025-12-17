def test_list_page_contains_csrf_token_and_form_fields(client):
    res = client.get('/')
    assert res.status_code == 200
    content = res.content.decode()
    # the rendered template should include the csrf input and the form input
    assert 'name="csrfmiddlewaretoken"' in content
    assert 'Enter task title' in content or 'name="title"' in content