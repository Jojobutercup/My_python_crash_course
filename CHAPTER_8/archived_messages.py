def send_messages(short_text, sent_messages):
    """Simulating text messages, until none are left"""
    while short_text:
        processing_text = short_text.pop()
        print(f"Typing.....\n{processing_text}")
        sent_messages.append(processing_text)

def show_message(short_text):
    """Passing a list to a fuunction that shows a complete sentence"""
    print(f"\nThese are a list of text in my remaining in my collection:")
    for text in short_text:
        print(text.title())


short_text = ['love', 'beauty', 'rich', 'success', 'blessings', 'lucky']
sent_messages = []
send_messages(short_text[:], sent_messages)
show_message(short_text)
