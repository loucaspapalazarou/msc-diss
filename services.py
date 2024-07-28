import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from lightning import Callback

BODY: str = """
Hello,

The training for the model {module} has been completed.

Details:
- Final Epoch: {final_epoch}
- Total Steps: {total_steps}

Metrics:
"""


class EmailCallback(Callback):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def on_train_end(self, trainer, pl_module):
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = self.email
        msg["To"] = self.email
        msg["Subject"] = f"Training for {pl_module.__class__.__name__} completed"

        # Gather detailed training information
        final_epoch = trainer.current_epoch
        total_steps = trainer.global_step
        metrics = trainer.callback_metrics

        # Format the body of the email
        body = BODY.format(pl_module.__class__.__name__, final_epoch, total_steps)

        for key, value in metrics.items():
            if isinstance(value, float):
                value = f"{value:.4f}"
            body += f"- {key}: {value}\n"

        body += "\nBest regards,\nYour Training System"

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, "plain"))

        # Set up the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.email, self.password)

        # Send the email
        server.sendmail(self.email, self.email, msg.as_string())

        # Quit the server
        server.quit()
