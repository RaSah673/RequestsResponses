from django.db import migrations

def create_data(apps, schema_editor):
    Snippet = apps.get_model('snippets', 'Snippet')
    Snippet(title="code snippets are important", code="class Migration(migrations.Migration):", linenos="True", language="actionscript").save()

class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]