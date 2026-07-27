# Publishing new lessons

Publish future lessons in small, focused commits so the project history remains
easy to follow.

## Before publishing

1. Add a Markdown introduction and learning objective.
2. Use the portable `python3` notebook kernel.
3. Restart the kernel and run the lesson from top to bottom.
4. Clear all saved cell outputs.
5. Run the repository validator:

   ```powershell
   python tools/validate_notebooks.py
   ```

## Publish one lesson

Replace the example filename and lesson title:

```powershell
git add New_Python_Lesson.ipynb README.md
git commit -m "Add new Python lesson"
git push origin main
```

Only stage the new lesson and its README curriculum update. GitHub Actions will
run the notebook checks after the push. Confirm that CI passes before publishing
the next lesson.
