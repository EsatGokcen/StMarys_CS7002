# Client Code
from basic_task import BasicTask
from important_task import ImportantTask
from reminder_decorator import ReminderDecorator
from attachment_decorator import AttachmentDecorator
import datetime

def main():
    # Create basic task
    basic_task = BasicTask("Discuss project status", datetime.datetime(2024, 3, 25))

    # Add reminder to the basic task
    task_with_reminder = ReminderDecorator(basic_task, datetime.datetime(2024, 3, 24))

    # Create important task
    important_task = ImportantTask("Prepare presentation slides", datetime.datetime(2024, 3, 20))

    # Add reminder and attachment to the important task
    important_task_with_reminder_and_attachment = AttachmentDecorator(
        ReminderDecorator(important_task, datetime.datetime(2024, 3, 19)), "presentation.pdf"
    )

    # Display task details
    print("Task 1: Basic Task with Reminder")
    print("Description:", task_with_reminder.get_description())
    print("Deadline:", task_with_reminder.get_deadline())
    print("Reminder:", task_with_reminder.get_reminder())
    print()

    print("Task 2: Important Task with Reminder and Attachment")
    print("Description:", important_task_with_reminder_and_attachment.get_description())
    print("Deadline:", important_task_with_reminder_and_attachment.get_deadline())
    print("Reminder:", important_task_with_reminder_and_attachment._task.get_reminder())
    print("Attachment:", important_task_with_reminder_and_attachment.get_attachment())

if __name__ == "__main__":
    main()