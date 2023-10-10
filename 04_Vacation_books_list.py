num_pages_in_book = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

num_pages_per_hour = num_pages_in_book / pages_per_hour
hours_per_day = num_pages_per_hour / days_to_read

print(round(hours_per_day))
