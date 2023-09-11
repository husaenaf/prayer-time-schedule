import bs4
import requests

def ekstraksi_data():
    try:                #  try = menempatkan kode yang dapat menimbulkan kesalahan
        url = 'https://www.jadwalsholat.org/adzan/monthly.php?id=250'
        contents = requests.get(url)
    except Exception:   #  except Exception = menangkap semua jenis kesalahan yang terjadi dalam blok try
        return None

# 1. parsing/mengurai HTML dari suatu sumber web
    if contents.status_code == 200:
        soup = bs4.BeautifulSoup(contents.text, 'html.parser')
        data = soup.find_all('tr','table_highlight')

# 2. ekstraksi/mengambil data dari hasil parsing
        prayer = {}
        for row in data:
            columns = row.find_all('td')
            if len(columns) >= 7:
                date = columns[0].text
                imsak = columns[1].text
                subuh = columns[2].text
                terbit = columns[3].text
                dzuhur = columns[4].text
                ashar = columns[5].text
                maghrib = columns[6].text
                isya = columns[7].text
    else:
        return None

# 3. menampilkan data
    # 1. mengorganisasi dan menyimpan data / untuk mengisi dictionary(json) dalam 1 tanggal tertentu
    prayer[date] = {
        'Imsak': imsak,
        'Subuh': subuh,
        'Terbit': terbit,
        'Dzuhur': dzuhur,
        'Ashar': ashar,
        'Maghrib': maghrib,
        'Isya': isya
    }
    # 2. menampilkan dengan perulangan/iterasi yang diambil dari dictionary yang sudah dibuat sebelumnya
    for name, prayer_time in prayer[date].items():
        print(f"{name} : {prayer_time}")