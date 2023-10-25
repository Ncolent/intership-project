from behave import given, when, then


@then('Verify the right page opens.')
def verify_off_plan_opened(context):
    context.app.off_plan_page.verify_off_plan()

@then('Filter by sale status of Last Units.')
def filter_last_units(context):
    context.app.off_plan_page.filter_by_last_units()

@then('Verify each product contains the Last Units tag')
def verify_each_item_last_unit(context):
    context.app.off_plan_page.verify_each_item_last_unit()

