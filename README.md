# IB School Odoo Suite

Generated repository skeleton for IB School (18 modules).

Generated on 2025-11-15T16:52:00.464022

## Modules included

- ibschool_core
- ibschool_academic
- ibschool_management
- ibschool_attendance
- ibschool_grading
- ibschool_fees
- ibschool_transport
- ibschool_communication
- ibschool_library
- ibschool_discipline
- ibschool_hrm
- ibschool_lms_portal
- ibschool_ai_chatbot
- ibschool_innovation_lab
- ibschool_analytics
- ibschool_admissions
- ibschool_integration_managebac
- ibschool_dashboard

## How to use

1. Copy this folder to your Odoo addons path.
2. Restart Odoo and update app list.

Hướng dẫn sử dụng IBSchool Odoo trên Windows Server
# IBSchool Odoo 19 – Hướng dẫn sử dụng trên Windows Server

## 1. Yêu cầu môi trường

- Windows Server 2019/2022 hoặc tương tự
- Python 3.11+
- Git
- Odoo 19 source code (ví dụ: `C:\sna\odoo-19.0`)
- Virtual environment cho Odoo (`odoo-venv`)

---

## 2. Cài đặt Odoo trong Virtual Environment

1. Mở PowerShell và tạo venv:

```powershell
cd C:\sna\odoo-19.0
python -m venv odoo-venv


Kích hoạt venv:

C:\sna\odoo-19.0\odoo-venv\Scripts\Activate.ps1


Cài dependencies:

pip install --upgrade pip
pip install -r requirements.txt

3. Cấu hình Odoo

File odoo.conf ví dụ:

[options]
addons_path = C:\sna\ibschool_repo
db_host = localhost
db_port = 5432
db_user = odoo
db_password = odoo
xmlrpc_port = 8069
logfile = C:\sna\odoo-19.0\odoo.log

4. Chạy Odoo lần đầu
C:\sna\odoo-19.0\odoo-venv\Scripts\Activate.ps1
python C:\sna\odoo-19.0\odoo-bin -c C:\sna\odoo-19.0\odoo.conf


Truy cập: http://localhost:8069

Tạo database mới nếu cần.

5. Cập nhật code từ GitHub và restart Odoo tự động
5.1 Tạo script PowerShell update_odoo.ps1:
Param(
    [string]$branch = "develop"
)

Write-Host "Updating IBSchool repo on branch $branch..."

Set-Location "C:\sna\ibschool_repo"

git fetch
git checkout $branch
git pull origin $branch

# Activate venv
$env:VIRTUAL_ENV = "C:\sna\odoo-19.0\odoo-venv"
$env:PATH = "$env:VIRTUAL_ENV\Scripts;$env:PATH"

# Stop Odoo cũ nếu đang chạy
$odooProcess = Get-Process -Name python -ErrorAction SilentlyContinue | Where-Object { $_.Path -like "*odoo-bin*" }
if ($odooProcess) {
    Write-Host "Stopping existing Odoo process..."
    $odooProcess | Stop-Process -Force
    Start-Sleep -Seconds 3
}

# Start Odoo mới
Write-Host "Starting Odoo..."
Start-Process -NoNewWindow -FilePath "python" -ArgumentList "C:\sna\odoo-19.0\odoo-bin -c C:\sna\odoo-19.0\odoo.conf"

Write-Host "Odoo updated and restarted successfully!"

5.2 Cách sử dụng

Cập nhật develop:

.\update_odoo.ps1 -branch develop


Cập nhật master (production):

.\update_odoo.ps1 -branch master

6. Quy trình làm việc với GitHub

Feature branch:

git checkout develop
git pull
git checkout -b feature/<tên_module>


Làm việc và commit theo conventional commit:

feat: thêm module Library
fix: sửa bug import dữ liệu
refactor: tách model Student
docs: cập nhật README


Push branch lên GitHub → tạo Pull Request vào develop.

Reviewer check → merge vào develop.

Trên local server:

.\update_odoo.ps1 -branch develop


Khi develop ổn → merge vào master:

.\update_odoo.ps1 -branch master

7. Gợi ý nâng cao

Tạo Task Scheduler để script chạy tự động.

Backup database trước khi merge vào master.

Có thể kết hợp GitHub Actions để lint + test tự động.
