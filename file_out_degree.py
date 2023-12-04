#####################################
# ファイル名：　file_out_degree.py
# 座標から角度を求めるプログラム（2023/12/01作成）

# 使い方
# input_csv_path　にMid系を選択し，
# output_csv_path　に出力された列を，
# Mid系のプログラムから座標情報を読み取り，ドラッグごとの角度を別ファイルに出力します．
#
# 2列目（0から数えてるから-1列）と3列目に座標データが入っている想定なので，適宜変えること！
#
# 通常のxy座標で，x軸方向から±180°の範囲で角度が求められる．
# 空行も同じタイミングで入れてくれるよ．

#####################################


import csv
import math

def calculate_angle(start_x, start_y, end_x, end_y):
    # Calculate the angle between two points (start and end)
    angle_rad = math.atan2(end_y - start_y, end_x - start_x)
    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)
    print(f"The angle is: {angle_deg} degrees")
    return angle_deg


def process_drag(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Skip the header row
        header = next(reader)
        # Write header to output file
        writer.writerow(['degree'])

        drag_start = None
        prev_row = None  # Initialize prev_row outside the loop
        current_drag_count = 1
        
        for row in reader:
            # Check if the row is not empty
            if row and row[2] and row[3]:
            
                # Check if it's the start of a new drag
                if row[0] == '1':
                    # If this is not the first drag, write the previous drag's data
                    if prev_row is not None and drag_start is not None:
                        drag_end = (float(prev_row[2]), float(prev_row[3]))
                        angle_deg = calculate_angle(drag_start[0], drag_start[1], drag_end[0], drag_end[1])
                        writer.writerow([angle_deg])
                        current_drag_count += 1

                    # Start a new drag
                    drag_start = (float(row[2]), float(row[3]))

                elif not row[0] and drag_start is not None:
                    # If an empty cell is encountered, it marks the end of the current drag
                    if drag_start is not None:
                        drag_end = (float(row[2]), float(row[3]))
                        angle_deg = calculate_angle(drag_start[0], drag_start[1], drag_end[0], drag_end[1])
                        writer.writerow([angle_deg])
                        current_drag_count += 1

                # Keep track of the previous row
                prev_row = row
                
            # Output an empty line for each empty line in the input
            if not row[0]:
                print("空行")
                writer.writerow([])

        # Write the last drag's data if there was one
        if prev_row is not None and drag_start is not None:
            drag_end = (float(prev_row[2]), float(prev_row[3]))
            angle_deg = calculate_angle(drag_start[0], drag_start[1], drag_end[0], drag_end[1])
            writer.writerow([angle_deg])
            current_drag_count += 1

        print("Processing completed.")

# Example usage
input_csv_path = 'Data/test.csv'
output_csv_path = 'Data/_test_output.csv'
process_drag(input_csv_path, output_csv_path)