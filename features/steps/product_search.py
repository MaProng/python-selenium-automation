@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_result_page.verify_search_results(expected_item)


@then('Verify that URL has {partial_url}')
def verify_search_page_url(context, partial_url):
    context.app.base.verify_partial_url(partial_url)
    context.app.search_result_page.verify_partial_url(partial_url)