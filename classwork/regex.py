import re
import ssl
import urllib.request

# tel_nums = '(257) 563-7402 (257) 563-7402 (257) 563-7402'
# pattern = r'\(\d{3}\) \d{3}-\d{4}'
# match = re.findall(pattern, tel_nums)
# print(match)
#
ssl._create_default_https_context = ssl._create_unverified_context
# site = urllib.request.urlopen("https://www.summet.com/dmsi/html/codesamples/addresses.html").read().decode()
# print(site)

response = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry").read().decode()
print(response)
pattern = r"(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span class=\"spec__index-inner\">Телефон</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt class=\"spec__index\"><span class=\"spec__index-inner\">Часы работы</span></dt>\n*\s*<dd class=\"spec__value\"[^\w]*|<span class=\"org-widget-feedback__rate-count\">[^\w]*<p>[^\w]*|)([^<]*\b)"
match = re.findall(pattern, response)
match = [match[i:i+4] for i in range(0, len(match), 4)]
print(match)