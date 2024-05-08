Problems:
The task listed for RPA is quite ambigiuos in what actually user required from automation which should be clarified
before creating automation. Main problems during this task was to decide where user input should be required to stop
automation. For example steps ranging from username choices, what needs to be added to the cart should be left up for
user to decide. However, taking into consideraion that even with these two stops automation loses it's value, I've
decided to describe what could be changed on each step for user input to be added but it should require business
analyst or actual users input to make the program targeted.

Note, that I skipped creating UI due to time increase on the task and did everything on console with clear distinction
of where to choose each option.

What has not been done:
1. Testing other users and updating the code to reflect each possible outcome to the code. In this case only
standard user was used.
2. Clarifying on which points user interaction is required (i.e. username selection, cart items selection, etc) and
creating simple popups where needed.
3. Instead of using predefined strings/lists, there should be functions/methods to extract the information directly
from website (i.e. item_id_list)
4. Either having default values or other file containing contact information filed out during checkout.
5. Testing