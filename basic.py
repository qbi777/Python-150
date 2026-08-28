#testing branch topic
import sys
import threading
import ui_library_v2
from ui_library_v2 import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer
from PyQt5 import QtGui
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

# Additional imports for barcode scanner handling
import sys

# Your existing setup for the Google Sheets API and RFID
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/pi/Downloads/service_account.json', scope)

client = gspread.authorize(creds)
sheet_name = 'pythonedit'
worksheet_name = 'Sheet3'
sheet = client.open(sheet_name).worksheet(worksheet_name)
all_cells = sheet.get_all_values()

top_lines = ""
bottom_lines = ""

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()  # Assuming Ui_MainWindow is from the ui_library_v2
        self.ui.setupUi(self)

        # Set IP addresses as instance variables
        self.for_A_B = "172.20.10.3"  # Example IP Address
        self.for_C_D = "172.20.10.4"   # Example IP Address

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_rfid_and_image)
        self.timer.start(3000)

        # Start a thread to listen for barcode scanner input
        self.barcode_thread = threading.Thread(target=self.listen_for_barcode)
        self.barcode_thread.daemon = True
        self.barcode_thread.start()

    def listen_for_barcode(self):
        while True:
            # Listen for input from the barcode scanner
            barcode_data = input().strip()  # Assuming barcode scanner input appears like normal input
            self.process_barcode_input(barcode_data)
    
    # Function to send a letter to NodeMCU
    import requests

    def send_letter_to_nodemcu(ip_address, letter):
        url = f"http://{ip_address}/receive"
        data = {'letter': letter}
        try:
            response = requests.post(url, data=data)
            if response.status_code == 200:
                print(f"Letter '{letter}' sent successfully to NodeMCU at {ip_address}.")
            else:
                print(f"Failed to send the letter '{letter}' to NodeMCU at {ip_address}.")
        except requests.RequestException as e:
            print(f"Error in sending: {e}")

    def process_barcode_input(self, barcode_data):
        # This method sets the value of text_to_find based on barcode_data
        text_to_find = barcode_data.replace(" ", "")
        
        # Flag to track if a match is found
        match_found = False

        # The rest of your logic that depends on text_to_find goes here
        for row_idx, row in enumerate(all_cells, start=1):
            for col_idx, cell_value in enumerate(row, start=1):
                if text_to_find in cell_value:
                    match_found = True  # Set flag if a match is found
                    lines = cell_value.split('\n')
                    top_lines = '\n'.join(lines[1:4])
                    bottom_lines = '\n'.join(lines[-3:])

                    # Based on the column, update the GUI
                    if col_idx == 1:
                        self.ui.left_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-LEFT-removebg-preview.png"))
                        self.ui.left_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-LEFT-removebg-preview.png"))
                        self.ui.left_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-LEFT-removebg-preview.png"))
                        self.ui.label_text_space_1.setText(top_lines)
                        self.ui.label_text_space_2.setText(bottom_lines)
                        self.ui.right_side_shell_top.clear()
                        self.ui.right_side_shell_mid.clear()
                        self.ui.right_side_shell_down.clear()
                        self.send_letter_to_nodemcu(for_A_B, 'L1')
                        self.send_letter_to_nodemcu(for_C_D, 'Nan')
                    
                    elif col_idx == 2:
                        self.ui.left_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-LEFT-removebg-preview.png"))
                        self.ui.left_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-LEFT-removebg-preview.png"))
                        self.ui.left_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-LEFT-removebg-preview.png"))
                        self.ui.label_text_space_1.setText(top_lines)
                        self.ui.label_text_space_2.setText(bottom_lines)
                        self.ui.right_side_shell_top.clear()
                        self.ui.right_side_shell_mid.clear()
                        self.ui.right_side_shell_down.clear()
                        self.send_letter_to_nodemcu(for_A_B, 'L4')
                        self.send_letter_to_nodemcu(for_C_D, 'Nan')


                    elif col_idx == 3:
                        self.ui.right_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-RIGHT-removebg-preview.png"))
                        self.ui.right_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-RIGHT-removebg-preview.png"))
                        self.ui.right_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-RIGHT-removebg-preview.png"))
                        self.ui.label_text_space_1.setText(top_lines)
                        self.ui.label_text_space_2.setText(bottom_lines)
                        self.ui.left_side_shell_top.clear()
                        self.ui.left_side_shell_mid.clear()
                        self.ui.left_side_shell_down.clear()
                        self.send_letter_to_nodemcu(for_C_D, 'L1')
                        self.send_letter_to_nodemcu(for_A_B, 'Nan')

                    elif col_idx == 4:
                        self.ui.right_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-RIGHT-removebg-preview.png"))
                        self.ui.right_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-RIGHT-removebg-preview.png"))
                        self.ui.right_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/arrow_lib-RIGHT-removebg-preview.png"))
                        self.ui.label_text_space_1.setText(top_lines)
                        self.ui.label_text_space_2.setText(bottom_lines)
                        self.ui.left_side_shell_top.clear()
                        self.ui.left_side_shell_mid.clear()
                        self.ui.left_side_shell_down.clear()
                        self.send_letter_to_nodemcu(for_C_D, 'L4')
                        self.send_letter_to_nodemcu(for_A_B, 'Nan')

                    break  # Exit the inner loop if a match is found

            if match_found:
                break  # Exit the outer loop if a match is found

        # If no match was found, execute the following
        if not match_found:
            self.ui.left_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_right.png"))
            self.ui.left_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_right.png"))
            self.ui.left_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_right.png"))
            self.ui.right_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_right.png"))
            self.ui.right_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_right.png"))
            self.ui.right_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_right.png"))
            self.ui.left_side_shell_top.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_left.png"))
            self.ui.left_side_shell_mid.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_left.png"))
            self.ui.left_side_shell_down.setPixmap(QtGui.QPixmap("/home/pi/Desktop/kits_library/nor_arrow_left.png"))
            self.ui.label_text_space_1.setText("")
            self.ui.label_text_space_2.setText("Book does not belong to this system")
            self.send_letter_to_nodemcu(for_A_B, 'Nan')
            self.send_letter_to_nodemcu(for_C_D, 'Nan')
    def update_rfid_and_image(self):
        # Your existing update logic goes here
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
