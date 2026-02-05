import os


def move_file(command: str) -> None:
    try:
        if not isinstance(command, str):
            raise ValueError(
                "Input must be a string formatted as: 'cp <source> <target>'"
            )

        parts = command.strip().split()
        if len(parts) != 3 or parts[0] != "mv":
            raise ValueError(
                f"Invalid command: '{command}'. Expected: "
                "'cp <source> <target>'"
            )

        _, source, target = parts

        if source == target:
            return

        if not os.path.exists(source):
            raise OSError("Source file does not exist")

        target_path = "/".join(target.split("/")[:-1])
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        with open(source, "r") as file_in, open(target, "w") as file_out:
            file_out.write(file_in.read())

        os.remove(source)

    except ValueError as e:
        print(
            "Invalid input. Expected format: 'cp <source> <target>'. "
            f"Got: '{command}'.",
            e,
        )
    except OSError as e:
        print(f"Error processing file copy: {e}. Command: '{command}'")


move_file("mv text.txt first_dir/second_dir/third_dir/file2.txt")
