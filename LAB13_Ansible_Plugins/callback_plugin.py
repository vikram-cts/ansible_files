from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'custom_callback'

    def v2_playbook_on_start(self, playbook):
        self._display.display("My Playbook is starting...")

    def v2_playbook_on_stats(self, stats):
        self._display.display("My Playbook is finished...")

    # This method is triggered when a task fails
    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = result._host  # Get the name of the host where the task failed
        task_name = result.task_name  # Get the name of the failed task
        error_message = result._result.get('msg', 'No error message')  # Capture the error message
        
        # Display the failure message
        self._display.display(f"Task '{task_name}' failed on host '{host.name}' with error: {error_message}")

        # You could also send this message to external services like Slack, a logging system, etc.
