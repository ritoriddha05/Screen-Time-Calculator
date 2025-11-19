# --- CONSOLIDATED SCREEN TIME CALCULATOR ---

# 1. INITIAL DATA SETUP (Simulating persistence without file I/O imports)
# Logs are stored as a list of dictionaries.
LOGS = [
    {"category": "Academics", "duration": 60.0, "date_time": "2025-11-19 10:00:00"},
    {"category": "Social Media", "duration": 120.0, "date_time": "2025-11-19 11:00:00"},
    {"category": "Entertainment", "duration": 30.0, "date_time": "2025-11-19 12:00:00"}
]
CATEGORIES = ["Academics", "Social Media", "Entertainment", "Communication", "Other"]
PRODUCTIVE_CATEGORIES = ["Academics"]

running = True
print("Welcome to the Digital Wellness Tracker!")

# MAIN APPLICATION LOOP
while running:
    # DISPLAY MENU
    print("\n--- Digital Wellness Tracker ---")
    print("1. Log New Screen Time")
    print("2. View Dashboard (Analytics)")
    print("3. Manage Logs (CRUD)")
    print("4. Exit (Data will NOT be saved in this basic version)")
    print("----------------------------------")
    
    choice = input("Enter your choice (1-4): ")

    # --- 1. LOG NEW SCREEN TIME (Data Input Module) ---
    if choice == '1':
        print("\n--- Log New Screen Time ---")
        print("Categories:", ", ".join(CATEGORIES))
        
        category = input("Enter category: ").strip()
        
        if category not in CATEGORIES:
            print("Warning: Category not recognized. Using 'Other'.")
            category = "Other"

        # Basic input validation (replacing try/except)
        duration_input = input("Enter duration (in minutes): ")
        
        # Simple check for numeric and positive value
        if duration_input.isdigit():
            duration = float(duration_input)
            if duration > 0:
                # SIMULATING DATE/TIME without import
                current_time = "SIMULATED_TIME" 
                
                new_entry = {"category": category, "duration": duration, "date_time": current_time}
                LOGS.append(new_entry)
                print(f"\nSUCCESS: Logged {duration} minutes for {category}!")
            else:
                print("Error: Duration must be a positive number.")
        else:
            print("Error: Invalid input. Please enter a number for duration.")

    # --- 2. VIEW DASHBOARD (Processing & Reporting Modules) ---
    elif choice == '2':
        print("\n--- Screen Time Dashboard ---")
        
        if len(LOGS) == 0:
            print("No data available to analyze.")
            
        else:
            # Calculation Logic (Replacing ProcessingEngine)
            total_time = 0.0
            category_summary = {}
            productive_time = 0.0
            unproductive_time = 0.0

            for entry in LOGS:
                duration = entry["duration"]
                category = entry["category"]
                
                total_time = total_time + duration
                
                # Summarize by category
                if category not in category_summary:
                    category_summary[category] = 0.0
                category_summary[category] = category_summary[category] + duration
                
                # Analyze productivity
                if category in PRODUCTIVE_CATEGORIES:
                    productive_time = productive_time + duration
                else:
                    unproductive_time = unproductive_time + duration

            print(f"\nTOTAL LOGGED TIME: {total_time:.2f} minutes ({total_time / 60:.2f} hours)")
            print("-" * 30)

            # Reporting/Visualization (Simple Text Output)
            print("CATEGORY BREAKDOWN:")
            
            # Simple sorting simulation (requires Python 3.7+ dictionary order preservation)
            sorted_categories = sorted(category_summary.items(), key=lambda item: item[1], reverse=True)
            
            if len(category_summary) > 0:
                max_val = max(category_summary.values())
            else:
                max_val = 1
            
            for category, total in sorted_categories:
                hours = total / 60
                bar_length = int((total / max_val) * 20)
                bar = "#" * bar_length
                print(f"  {category:<15}: {hours:6.2f} hours | {bar}")

            print("-" * 30)
            
            print(f"PRODUCTIVITY ANALYSIS:")
            print(f"  Productive Time (Academics): {productive_time / 60:.2f} hours")
            print(f"  Unproductive Time (Others): {unproductive_time / 60:.2f} hours")

    # --- 3. MANAGE LOGS (CRUD Module) ---
    elif choice == '3':
        print("\n--- Manage Logs (CRUD) ---")
        if len(LOGS) == 0:
            print("No logs found.")
        else:
            print("ID | Category | Duration (min) | Date/Time")
            print("-" * 40)
            log_index = 0
            while log_index < len(LOGS):
                entry = LOGS[log_index]
                print(f"{log_index:<2} | {entry['category']:<10} | {entry['duration']:<14.2f} | {entry['date_time']}")
                log_index = log_index + 1
            print("-" * 40)

            action = input("Enter 'e' to Edit, 'd' to Delete, or 'b' to Go Back: ").lower()
            
            if action != 'b':
                log_id_input = input("Enter the ID of the log to modify: ")
                
                # Simple ID validation
                if log_id_input.isdigit():
                    log_id = int(log_id_input)
                    if 0 <= log_id < len(LOGS):
                        
                        # EDIT (Update)
                        if action == 'e':
                            entry = LOGS[log_id]
                            print(f"Editing Log ID {log_id}: Category={entry['category']}, Duration={entry['duration']}")
                            new_duration_str = input("Enter new duration (press Enter to skip): ")
                            if len(new_duration_str) > 0 and new_duration_str.replace('.', '', 1).isdigit():
                                new_duration = float(new_duration_str)
                                if new_duration > 0:
                                    entry['duration'] = new_duration
                                    entry['date_time'] = "SIMULATED_TIME_UPDATED"
                                    print("SUCCESS: Log updated.")
                                else:
                                    print("Error: Duration must be positive.")
                            else:
                                print("Skipping duration update or invalid format.")
                        
                        # DELETE
                        elif action == 'd':
                            confirm = input(f"Are you sure you want to delete log ID {log_id}? (y/n): ").lower()
                            if confirm == 'y':
                                # Simulating deletion without the 'del' keyword (more complex, using list reconstruction)
                                new_logs = []
                                current_index = 0
                                while current_index < len(LOGS):
                                    if current_index != log_id:
                                        new_logs.append(LOGS[current_index])
                                    current_index = current_index + 1
                                LOGS = new_logs
                                print("SUCCESS: Log deleted.")
                        
                        else:
                            print("Invalid action.")
                    else:
                        print("Invalid log ID.")
                else:
                    print("Invalid input for ID.")
    
    # --- 4. EXIT ---
    elif choice == '4':
        print("Exiting application.")
        running = False
    
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
