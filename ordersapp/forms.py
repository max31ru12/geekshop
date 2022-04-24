class OrderItemForm(forms.ModelForm):
    price = forms.CharField(label="цена", required=False)

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = OrderItem
        exclude = ()