# mdmenumd

A script tool to generate markdown form menu with links from a folder of markdown files

## Usage

   ```sh
   python mdmenumd.py <folder_path> <file_suffix> [--md_filename <generated_menu_markdown_file_name>]
   ```

   ```sh
   python mdmenumd.py /path/to/folder .txt
   ```

   ```sh
   python mdmenumd.py /path/to/folder .txt --md_filename my_directory.md
   ```

For example, if you do as follows:

   ```sh
   python mdmenumd.py ./ .md 
   ```

You will get a markdown file named `directory.md` in the current directory with the following content:

```markdown
# List of Files

- [directory.md](directory.md)
- [README.md](README.md)
- licensing
  - [List_of_Disqualified_Entities.md](licensing\List_of_Disqualified_Entities.md)
  - [List_of_Observing_Entities.md](licensing\List_of_Observing_Entities.md)
  - [Mizumoto.General.Public.License.v1.5.md](licensing\Mizumoto.General.Public.License.v1.5.md)
  - [mpl-v2.0.md](licensing\mpl-v2.0.md)
```
