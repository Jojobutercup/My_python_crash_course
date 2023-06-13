def show_message(short_text):
    """Passing a list to a fuunction that shows a complete sentence"""
    print(f"This are a list of text in my collection:")
    for text in short_text:
        print(text.title())


short_text = ['love', 'beauty', 'rich', 'success', 'blessings', 'lucky']
show_message(short_text)
