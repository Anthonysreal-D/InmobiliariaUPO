/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState } = owl;

class C1Componente extends Component {
    setup() {
        this.state = useState({value:1});
    }
}
    
C1Componente.template = 'owl.C1Componente';
registry.category('actions').add('owl.action_C1Componente_js', C1Componente);