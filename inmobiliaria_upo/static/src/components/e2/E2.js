/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState } = owl;

class E2Componente extends Component {
    setup() {
        this.state = useState({value:1});
    }
}
    
E2Componente.template = 'owl.E2Componente';
registry.category('actions').add('owl.action_E2Componente_js', E2Componente);