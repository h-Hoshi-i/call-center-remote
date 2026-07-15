def combine(lines) -> str:
    email = "\n".join(lines)
    return email

def select_email(selection, stu_name:str="Student", user_name="Nathaniel"):
    base = [
        f"Hello {stu_name},",
        "",
        "Thank you for reaching out to Southern.",
        "",
        "If you have any other questions please email admisions@southern.edu or call 1-800-SOUTHERN.",
        "",
        "God Bless,",
        "Your Admissions Team",
        f"{user_name}",
        ]
    prev_en_stu_2026 = [
        """<html>""",
        """  <head>""",
        """    <title></title>""",
        """  </head>""",
        """  <body>""",
        """    <p>""",
        f"""      Hello {stu_name},""",
        """    </p>""",
        """""",
        """    <p>""",
        """      At Southern Adventist University, we believe every educational journey deserves the opportunity for completion. We'd love to reconnect and help you finish the degree you started.""",
        """    </p>""",
        """""",
        """    <p>""",
        """      Eligible returning students may qualify for a renewable <b>$3,000 scholarship</b>, along with updated scholarship and financial aid opportunities. We've also expanded our evening and online course offerings, providing greater flexibility to fit your education into your current lifestyle.""",
        """    </p>""",
        """""",
        """    <p>""",
        """      To help you get started, please complete the &nbsp;<a href="https://www.southern.edu/undergrad/admissions/reactivate.html">Reactivation Form</a>. Reactivating your account before contacting us will help expedite the process.""",
        """    </p>""",
        """""",
        """    <p>""",
        """      Whether you're ready to return or simply exploring your options, our <b>First Year Experience</b> team is here to answer your questions, review your options, and guide you through every step of the process.&nbsp;<strong>Schedule&nbsp;your appointment with them</strong>&nbsp;<a href="https://admissions.e.southern.edu/portal/advising" rel="noreferrer noopener" target="_blank">here.</a>""",
        """    </p>""",
        """""",
        """    <p>""",
        """      Registration for <b>Fall 2026</b> is already underway, and course availability is filling quickly. Reaching out early can help ensure access to the courses, resources, and returning-student support that best meet your needs.""",
        """    </p>""",
        """""",
        """    <p>""",
        """      We would love the opportunity to help you take the next step toward completing your degree. To learn more, please call <b>1-800-SOUTHERN</b> or email <a href="mailto:fye@southern.edu"><b>fye@southern.edu</b></a>.""",
        """    </p>""",
        """""",
        """    <p>""",
        """      We look forward to reconnecting with you.""",
        """    </p>""",
        """""",
        """    <p>""",
        """      <br />""",
        """      God Bless,""",
        """    </p>""",
        """""",
        """    <p>""",
        """      The Admissions Team ~<br />""",
        """      Southern Adventist University <br />""",
        f"""      {user_name}""",
        """    </p>""",
        """""",
        """    <p>""",
        """    </p>""",
        """  </body>""",
        """</html>""",
        ]
    if selection == "base":
        return combine(base)
    if selection == "previous2026":
        return combine(prev_en_stu_2026)


