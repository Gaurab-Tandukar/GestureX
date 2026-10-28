from pathlib import Path
import cv2

flag = False
VALID_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

print("================================== Enter q to quit ====================================")
while not flag:
    fileLocation = input("Give the file location of the image: ").strip()

    if fileLocation.lower() == "q":
        print("Come again")
        flag = True
        continue

    if not fileLocation:
        print("No file location provided. Please try again.")
        continue

    # Convert string to Path object to safely check the extension
    path = Path(fileLocation)

    # Check extension
    if path.suffix.lower() not in VALID_EXTENSIONS:
        print(
            f"Invalid extension '{path.suffix}'. Allowed extensions are:"
            f" {VALID_EXTENSIONS}"
        )
        continue

    # Check if the file actually exists on disk
    if not path.is_file():
        print("Error: The file does not exist. Please check the path.")
        continue

    # Read the image using OpenCV
    image = cv2.imread(str(path))

    # OpenCV returns None if it fails to load the image
    if image is None:
        print("Error: Failed to read the image. The file might be corrupted.")
    else:
        print("Success: Image loaded successfully!")
        # image processing here
        # --- Interactive Menu Based on Your Choice Input ---
        print("Choose an action:")
        print("  1. Convert to Grayscale and save")
        print("  2. Display original Image ")

        flag2 = False
        while not flag2:
            choice = input("Enter what you want to do (or 'q' to quit): ").strip()

            # 1. Check 'choice'
            if choice.lower() == 'q':
                print("Come again")
                flag = True
                flag2 = True
                break

            if choice == '1':
                grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                if grayImage is not None:
                    cv2.imwrite("grayScale.jpg", grayImage)
                else:
                    print("Failed to grayscale the image")
                flag2 = True
                continue

            elif choice == '2':
                cv2.imshow("Gray Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                flag2 = True
                continue

            else:
                print("enter valid choice")