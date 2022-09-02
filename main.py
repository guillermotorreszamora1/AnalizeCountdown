import csv
from datetime import datetime
from datetime import timedelta
def timediff(date, diff_string):
  if diff_string == None:
    return None
  diff_list = diff_string.split(':')
  if len(diff_list) == 1:
    delta = timedelta(hours=int(diff_list[0]))
  if len(diff_list) == 2:
    delta = timedelta(hours=int(diff_list[0]), minutes=int(diff_list[1]))
  if len(diff_list) == 3:
    delta = timedelta(hours=int(diff_list[0]), minutes=int(diff_list[1]), seconds=int(diff_list[2]))
  return date - delta

def format_date_line(start,finish, diff):
  date_diff = timedelta(hours=diff)
  start = start + date_diff
  sstart = start.strftime('.%d %H:%M:%S')
  if finish!=None:
    finish = finish + date_diff
    sfinish = finish.strftime('%H:%M:%S')
    result = sstart + '-' + sfinish
  else:
    result = sstart
  return result

def main():
  sstart_date = '2022-08-03 18:17'
  start_date = datetime.fromisoformat(sstart_date)
  offset_outputs = [-4,0,2]
  file = open('Artemis29S.csv')
  csv_reader = csv.reader(file)
  rows = []
  results_matrix = []
  for row in csv_reader:
    rows.append(row)
    result_row = []
    for row in rows:
      times = row[1].split('-')[1:]
      if len(times) == 2:
        start_time = times[0]
        end_time   = times[1]
      else:
        start_time = times[0]
        end_time   = None
    result_row.append(row[0])
    result_row.append(row[1])
    for offset_output in offset_outputs:
      result = format_date_line(timediff(start_date, start_time), timediff(start_date, end_time), offset_output)
      result_row.append(result)
    results_matrix.append(result_row)
  return results_matrix
result_file = open('result.csv','w')
csvwriter = csv.writer(result_file)
csvwriter.writerows(main())
print(main())
