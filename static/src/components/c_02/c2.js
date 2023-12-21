/** @odoo-module **/

import { registry } from '@web/core/registry';
const { Component, useState } = owl;

class C2Componente extends Component {
    setup() {
        this.state = useState({
            subastas: [],
        });

        this.dispatch = useDispatch();
        this.dispatch("loadSubastas");
    }

    async willStart() {
        this.state.subastas = await this.rpc({ model: 'inmobiliaria_upo.subasta', method: 'search_read', args: [[]], kwargs: { fields: ['name', 'valorInicial'] } });
    }
}

C2Componente.template = 'owl.C2Componente';
registry.category('actions').add('owl.action_C2Componente_js', C2Componente);

