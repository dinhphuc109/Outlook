import requests
from bs4 import BeautifulSoup

# URL của trang web bạn muốn cào
url = 'https://mail.thaco.com.vn/'

# Gửi yêu cầu HTTP đến URL
response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    # Phân tích HTML bằng BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lấy toàn bộ HTML và chuẩn bị lưu vào tệp
    html_content = soup.prettify()

    # Đường dẫn tệp lưu trữ dữ liệu
    file_path = 'output.txt'
    
    # Mở tệp để ghi (sẽ tự động tạo tệp nếu chưa tồn tại)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
        print(f'Data has been saved to {file_path}')
else:
    print("Failed to retrieve the web page")
