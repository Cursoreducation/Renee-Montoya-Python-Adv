class EmployeeFormController {
    constructor() {
        this.values = {
            email: {
                value: '',
                errors: [],
                required: true
            },
            name: {
                value: '',
                errors: [],
                required: true
            },
            departmentType: {
                value: '',
                errors: [],
                required: true
            },
            department: {
                value: '',
                errors: [],
                required: true
            }
        }

        this.employeeFormNode = null
        this.departmentTypeNode = null
        this.departmentIdNode = null

        this.init()
        this.addEventListeners()
    }

    init() {
        this.departmentTypeNode = document.getElementById('department_type')
        this.departmentIdNode = document.getElementById('department_id')
        this.employeeFormNode = document.getElementById('employee-form')

        this.departmentTypeNode.value = null
        this.departmentIdNode.value = null
    }

    addEventListeners() {
        this.departmentTypeNode.addEventListener('change', (evt) => this.handleDepartmentTypeChange(evt))
        this.employeeFormNode.addEventListeners('submit', (evt) => this.handleSubmit())
    }

    handleDepartmentTypeChange({ target }) {
        if (!target.value && !target.value.length > 0) {
            this.departmentIdNode.disabled = true
        }

        this.departmentIdNode.disabled = false

        this.values.departmentType.value = target.value
        this.departmentIdNode.value = null
        this.departmentIdNode.dataset.type = this.values.departmentType.value
    }

    validate() {}

    emailValidate(obj, field) {
        const regex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/g
        return obj[field].match(regex)
    }

    requireValidate(obj, field) {
        return obj[field] && this[field].length > 0
    }

    handleSubmit() {}
}

document.addEventListener('DOMContentLoaded', () => {
    new EmployeeFormController()
})
