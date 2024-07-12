emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],

              'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],

              'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],

              'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],

      	      'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],

      	      'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
emails = emails.items()
a = {i + '@' + k for k, v in emails for i in v}
a = '\n'.join(sorted(a))
print(a)

