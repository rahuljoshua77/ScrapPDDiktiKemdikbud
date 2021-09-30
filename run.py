import requests,json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def json_strategy(url):
    response = requests.get(f'{url}', verify=False)
    get_json = response.json()
    dumps_json = json.dumps(get_json)
    get_data = json.loads(dumps_json)
    return get_data

def data(choice, key):
    if choice == "1":
        api_url = f"https://api-frontend.kemdikbud.go.id/hit/{key}"
        comsume_api = json_strategy(api_url)
        dosen = comsume_api['dosen'][0]['text']
        detail_dosen = comsume_api['dosen'][0]['website-link']
        raw_link = detail_dosen.split('/')
        get_link = raw_link[2]
        api_url = f"https://api-frontend.kemdikbud.go.id/detail_dosen/{get_link}"
        comsume_api = json_strategy(api_url)
        get_data = comsume_api['dataumum']
        get_data_pdd = comsume_api['datapendidikan']
        print(f"[*] Data ditemukan: {dosen}")
        print(f"[*] ============== Detail ==============")
        print(f"[*] ID SDM: {get_data['id_sdm']}")
        print(f"[*] Tempat Lahir: {get_data['tmpt_lahir']}")
        print(f"[*] Status Keaktifan: {get_data['statuskeaktifan']}")
        print(f"[*] Pendidikan Tertinggi: {get_data['pend_tinggi']}")
        print(f"[*] Fungsional: {get_data['fungsional']}")
        print(f"[*] Ikatan Kerja: {get_data['ikatankerja']}")
        print(f"[*] ============== Riwayat Pendidikan ==============")
        for i in get_data_pdd:
            print(f"[*] Tahun Lulus: {i['thn_lulus']} - {i['nm_sp_formal']} - {i['namajenjang']} - {i['singkat_gelar']}")
        
    elif choice == "2":
        api_url = f"https://api-frontend.kemdikbud.go.id/hit_mhs/{key}"
        comsume_api = json_strategy(api_url)
        
        mahasiswa = comsume_api['mahasiswa'][0]['text']
        detail_mhs = comsume_api['mahasiswa'][0]['website-link']
        raw_link = detail_mhs.split('/')
        get_link = raw_link[2]
        api_url = f"https://api-frontend.kemdikbud.go.id/detail_mhs/{get_link}"
        comsume_api = json_strategy(api_url)
        get_data = comsume_api['dataumum']
        get_status = comsume_api['datastatuskuliah']
        idx_status = len(get_status) 
 
        get_studi = comsume_api['datastudi']
        idx_studi = len(get_studi)
        
        print(f"[*] Data ditemukan: {mahasiswa}")
        print(f"[*] ============ Detail ===========")
        print(f"[*] REG PD: {get_data['reg_pd']}")
        print(f"[*] Status Masuk: {get_data['nm_jns_daftar']}")
        print(f"[*] Status Mahasiswa: {get_status[idx_status-1]['nm_stat_mhs']}")
        print(f"[*] ============ Informasi Mata Kuliah Yang Diambil ============")
        semester = 1
        validator = []
        for i in range(idx_studi-1):
            clear_studi = get_studi[i]['nm_mk']
            get_semester = get_studi[i]['id_smt']
            datas_smstr = list(get_semester)
            get_listyear = datas_smstr[0:4]
          
            separat = ''
            idx_valid = len(validator)
            get_year = separat.join(get_listyear)
            try:
                if datas_smstr[4] == validator[idx_valid-1]:
                    pass
                else:
                    semester = semester + 1
            except:
                pass
            print(f"[*] {get_year} Semester {semester}: {clear_studi}")
            validator.append(datas_smstr[4])

    else:
        print('[*] Pilihan anda salah!')

def main():
    print("[*] Scrapping Data Dikti Kemdikbud")
    print("[*] 1. Dosen\n[*] 2. Mahasiswa")
    choice = input("[*] Masukin Pilihan (1/2): ")
    key = input("[*] Input Keyword Data: ")
    data(choice, key)

if __name__ == '__main__':
    main()
