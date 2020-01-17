from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(label="Name", max_length=32)

    status = forms.ChoiceField(
        label="Your status",
        choices=((1, "Not relevant"),
                 (2, "Review"),
                 (3, "Maybe relevant"),
                 (4, "Relevant"),
                 (5, "Leading candidate"))
    )

    message = forms.CharField(label='Message', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        user_name = cleaned_data.get('name')

        if len(user_name) < 2:
            msg = "Name must be at least 2 symbols long."
            self.add_error('name', msg)
            # raise forms.ValidationError(msg)
