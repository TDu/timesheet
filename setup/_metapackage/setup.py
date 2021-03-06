import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-timesheet",
    description="Meta package for oca-timesheet Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-crm_timesheet',
        'odoo12-addon-hr_timesheet_analysis',
        'odoo12-addon-hr_timesheet_employee_required',
        'odoo12-addon-hr_timesheet_role',
        'odoo12-addon-hr_timesheet_sheet',
        'odoo12-addon-hr_timesheet_task_required',
        'odoo12-addon-hr_utilization_analysis',
        'odoo12-addon-hr_utilization_report',
        'odoo12-addon-project_task_stage_allow_timesheet',
        'odoo12-addon-sale_timesheet_line_exclude',
        'odoo12-addon-sale_timesheet_task_exclude',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
