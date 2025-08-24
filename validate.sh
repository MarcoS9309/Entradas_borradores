#!/bin/bash

# Build and Quality Validation Script for Entradas_borradores Repository
# This script validates HTML, Python, JavaScript syntax and checks for common issues

echo "🔍 Starting repository validation..."
echo "================================="

# Check if we're in the right directory
if [ ! -f "README.md" ] || [ ! -d "_posts" ] || [ ! -d "_projects" ]; then
    echo "❌ Error: Not in the repository root directory"
    exit 1
fi

# Function to count files
count_files() {
    find "$1" -name "$2" 2>/dev/null | wc -l
}

# Repository statistics
echo "📊 Repository Statistics:"
echo "  - HTML files: $(count_files . '*.html')"
echo "  - Python files: $(count_files . '*.py')"
echo "  - JavaScript files: $(count_files . '*.js')"
echo "  - Markdown files: $(count_files . '*.md')"
echo "  - CSS files: $(count_files . '*.css')"
echo ""

# Validate HTML files
echo "🌐 Validating HTML files..."
python3 -c "
import html.parser
import os

class HTMLValidator(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.errors = []
        
    def error(self, message):
        self.errors.append(message)

all_valid = True
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                validator = HTMLValidator()
                validator.feed(content)
                if validator.errors:
                    print(f'❌ {filepath}: {len(validator.errors)} errors')
                    all_valid = False
                else:
                    print(f'✅ {filepath}')
            except Exception as e:
                print(f'⚠️  {filepath}: {e}')
                all_valid = False

exit(0 if all_valid else 1)
"

if [ $? -eq 0 ]; then
    echo "✅ All HTML files are valid"
else
    echo "❌ Some HTML files have issues"
fi
echo ""

# Validate Python files
echo "🐍 Validating Python files..."
python3 -c "
import ast
import os

all_valid = True
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                ast.parse(content)
                print(f'✅ {filepath}')
            except SyntaxError as e:
                print(f'❌ {filepath}: {e}')
                all_valid = False
            except Exception as e:
                print(f'⚠️  {filepath}: {e}')
                all_valid = False

exit(0 if all_valid else 1)
"

if [ $? -eq 0 ]; then
    echo "✅ All Python files are valid"
else
    echo "❌ Some Python files have issues"
fi
echo ""

# Validate JavaScript files (if node is available)
if command -v node &> /dev/null; then
    echo "📜 Validating JavaScript files..."
    js_valid=true
    for file in $(find . -name "*.js"); do
        if node -c "$file" 2>/dev/null; then
            echo "✅ $file"
        else
            echo "❌ $file: Syntax error"
            js_valid=false
        fi
    done
    
    if [ "$js_valid" = true ]; then
        echo "✅ All JavaScript files are valid"
    else
        echo "❌ Some JavaScript files have issues"
    fi
    echo ""
else
    echo "⚠️  Node.js not available, skipping JavaScript validation"
    echo ""
fi

# Check for required files
echo "📁 Checking required files..."
required_files=("README.md" "CONTRIBUTING.md" "DIRECTORY.md" "LICENSE" ".gitignore" "CHANGELOG.md")
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ Missing: $file"
    fi
done
echo ""

# Check for broken links in index.html
echo "🔗 Checking for potential broken links..."
if [ -f "index.html" ]; then
    # Check if referenced files exist
    grep -o 'href="[^"]*"' index.html | sed 's/href="//;s/"//' | while read -r link; do
        # Skip external links and anchors
        if [[ "$link" != http* && "$link" != "#"* && "$link" != mailto:* ]]; then
            if [ -f "$link" ] || [ -d "$link" ]; then
                echo "✅ Link exists: $link"
            else
                echo "⚠️  Potentially broken link: $link"
            fi
        fi
    done
fi
echo ""

echo "🎉 Repository validation completed!"
echo "================================="
# End of script
