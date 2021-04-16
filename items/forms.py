from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name*', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
    }))
    email = forms.EmailField(label='Email*', widget=forms.TextInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
    }))
    message = forms.CharField(label='Message*', widget=forms.Textarea(attrs={
        'placeholder': 'Your message',
        'class': 'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out'
    }))
