module.exports = {
    title: 'Doxybook Example Output',
    description: 'Doxybook example output converted to static website via vuepress',
    base: '/doxybook/vuepress/',
    themeConfig: {
        sidebar: 'auto',
        nav: [
            { text: 'Home', link: '/' },
            { text: 'Modules', link: '/api/modules' },
            {
                text: 'Classes',
                items: [
                    { text: 'Class List', link: '/api/annotated' },
                    { text: 'Class Index', link: '/api/classes' },
                    { text: 'Class Hierarchy', link: '/api/hierarchy' },
                    { text: 'Class Members', link: '/api/class_members' },
                    { text: 'Class Member Functions', link: '/api/class_member_functions' },
                    { text: 'Class Member Variables', link: '/api/class_member_variables' },
                    { text: 'Class Member Typedefs', link: '/api/class_member_typedefs' },
                    { text: 'Class Member Enumerations', link: '/api/class_member_enums' }
                ]
            },
            {
                text: 'Namespaces',
                items: [
                    { text: 'Namespace List', link: '/api/namespaces' },
                    { text: 'Namespace Members', link: '/api/namespace_members' },
                    { text: 'Namespace Member Functions', link: '/api/namespace_member_functions' },
                    { text: 'Namespace Member Variables', link: '/api/namespace_member_variables' },
                    { text: 'Namespace Member Typedefs', link: '/api/namespace_member_typedefs' },
                    { text: 'Namespace Member Enumerations', link: '/api/namespace_member_enums' }
                ]
            },
            { text: 'Files', link: '/api/files' },
            { text: 'Pages', link: '/api/pages' },
            { text: 'Bugs', link: '/api/bug' }
        ]
    }
}
