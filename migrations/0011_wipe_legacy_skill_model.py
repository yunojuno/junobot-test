from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0010_freelancercompanydetails_vat_reference_is_valid")
    ]

    operations = [
        migrations.RemoveField(model_name="skill", name="disciplines"),
        migrations.AlterUniqueTogether(name="skilldisciplines", unique_together=set()),
        migrations.RemoveField(model_name="skilldisciplines", name="discipline"),
        migrations.RemoveField(model_name="skilldisciplines", name="skill"),
        migrations.RemoveField(
            model_name="freelancerprofile", name="core_skills_deprecated"
        ),
        migrations.RemoveField(
            model_name="freelancerteam", name="core_skills_deprecated"
        ),
        migrations.DeleteModel(name="Skill"),
        migrations.DeleteModel(name="SkillDisciplines"),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300, unique=True)),
            ],
        ),
    ]