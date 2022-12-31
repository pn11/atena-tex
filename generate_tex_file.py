import json

def main():
    json_dict = json.load(open('addresses.json'))
    sender = json_dict['sender']
    sender_text = "\sendername{" + sender['name'] + "}\n" \
                + "\senderaddressa{" + sender['address_a'] + "}\n" \
                + "\senderaddressb{" + sender['address_b'] + "}\n" \
                + "\senderpostcode{" + sender['postal_code'] + "}"

    recipients = json_dict['recipients']
    recipients_text = ''

    for r in recipients:
        recipients_text += "\\addaddress{" + r['name'] + "}{" + r['title'] + "}{" + r['postal_code'] + "}{" + r['address_a'] + "}{" + r['address_b'] + "}\n"

    with open('template.tex.txt') as f:
        template = f.read()

    with open('out.tex', 'w') as f:
        f.write(template.replace('@@SENDER@@', sender_text).replace('@@RECIPIENTS@@', recipients_text) + '\n')

    with open('template_kansei.tex.txt') as f:
        template = f.read()

    with open('out_kansei.tex', 'w') as f:
        f.write(template.replace('@@SENDER@@', sender_text).replace('@@RECIPIENTS@@', recipients_text) + '\n')


if __name__ == '__main__':
    main()