from mako.template import Template


t = Template(filename="template.yml")
condition_fields = ["nid", "title"]
s = t.render(
    condition_fields=condition_fields
)
print(s)


