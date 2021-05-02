import requests
from bs4 import BeautifulSoup
import re


def search_profile(surname, firstname, fathername, birthyear):

    url = ('https://www.ypes.gr/wp-admin/admin-ajax.php?action=ekloges_pou_psifizeis&eid_ekl_ar='
        '&Eponymo={}&Onoma={}&on_pat={}&on_mht=&etos_gen={}&check_nation=gr'.format(surname,firstname,fathername,birthyear)
        )
    response = requests.get(url)

    if 'error.htm' in response.text:
        return False

    return {
        'surname': re.search(r'Επώνυμο :</td>\r\n\s+<td class="b">(.*?)</td>', response.text).group(1),
        'firstname': re.search(r'Όνομα :</td>\r\n\s+<td class="b">(.*?)</td>', response.text).group(1),
        'fathername': re.search(r'Όνομα Πατέρα :</td>\r\n\s+<td class="b">(.*?)</td>', response.text).group(1),
        'mothername': re.search(r'Όνομα Μητέρας :</td>\r\n\s+<td class="b">(.*?)</td>', response.text).group(1),
        'district': re.search(r'Νομός :</td>\r\n\s+<td class="b">(.*?)</td>', response.text).group(1),
        'birthyear': birthyear
    }


if __name__ == '__main__':

    surname = input('Type surname in Greek (required): ')
    firstname = input('Type first name in Greek (2+ characters are required): ')
    fathername = input('Type father\'s name in Greek (2+ characters or 0 for unknown): ')
    min_year = int(input('Type minimum birthyear (required): '))
    max_year = int(input('Type maximum birthyear (required): '))


    if fathername!='0':
        fathernames = [fathername]
    else:
        fathernames = ['ΓΕ', 'ΙΩ', 'ΚΩ', 'ΔΗ', 'ΝΙ', 'ΠΑ', 'ΒΑ', 'ΧΡ', 'ΑΘ', 'ΜΙ', 'ΕΥ', 'ΣΠ', 'ΑΝ', 'ΘΕ',
                     'ΧΑ', 'ΑΛ', 'ΕΜ', 'ΗΛ', 'ΣΤ', 'ΠΕ', 'ΣΩ', 'ΕΛ', 'ΑΠ', 'ΦΩ', 'ΔΙ', 'ΓΡ', 'ΑΓ', 'ΑΡ', 'ΛΕ']


    max_progress = (max_year-min_year+1)*len(fathernames)
    progress = 0

    found_profiles = []

    for birthyear in range(min_year, max_year + 1):
        for fathername in fathernames:

            res = search_profile(surname, firstname, fathername, birthyear)
            if res:
                found_profiles.append(res)

            progress += 1
            print('{} %'.format(int(100*progress/max_progress)))


    print('Results:\n')
    for profile in found_profiles:
        print(profile)
