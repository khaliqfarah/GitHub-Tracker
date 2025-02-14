import datetime
import calendar
from datetime import datetime, timedelta

def github_activity_tracker():
    """
    Helps track GitHub contribution goals and schedule reminders
    for maintaining consistent activity.
    """
    # Get current date and time
    current_date = datetime.now()
    
    # Calculate days remaining in the week
    current_weekday = current_date.weekday()
    days_remaining = 7 - current_weekday - 1
    
    # Track contributions this week
    def get_week_dates():
        week_start = current_date - timedelta(days=current_weekday)
        week_dates = []
        for i in range(7):
            date = week_start + timedelta(days=i)
            week_dates.append(date.strftime('%Y-%m-%d'))
        return week_dates
    
    def suggest_contribution_days():
        """Suggests evenly spaced days for contributions"""
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        suggested = weekdays[::2]  # Every other weekday
        return suggested
    
    # Print activity summary
    print("\nGitHub Activity Tracker")
    print("=====================")
    print(f"Current Date: {current_date.strftime('%Y-%m-%d')}")
    print(f"Current Weekday: {calendar.day_name[current_weekday]}")
    print(f"Days Remaining This Week: {days_remaining}")
    
    print("\nSuggested Contribution Schedule:")
    print("--------------------------------")
    for day in suggest_contribution_days():
        print(f"- {day}")
    
    print("\nRecommended Activities:")
    print("---------------------")
    print("1. Code reviews")
    print("2. Bug fixes")
    print("3. Documentation updates")
    print("4. Working on open issues")
    print("5. Adding tests")
    
    print("\nReminder: Quality > Quantity")
    print("Focus on meaningful contributions that add value to projects")

if __name__ == "__main__":
    github_activity_tracker()
