# controller_des.py
"""
A simple demo controller.
"""
import mosaik_api


META = {
    'type': 'event-based',
    'models': {
        'Ctrl': {
            'public': True,
            'params': [],
            'attrs': ['val_in', 'mod'],
        },
    },
}


class Controller(mosaik_api.Simulator):
    def __init__(self):
        super().__init__(META)
        self.agents = []

    def init(self, sid, time_resolution, output_delay=None):
        self.sid = sid
        self.output_delay = output_delay

        return self.meta

    def create(self, num, model):
        n_agents = len(self.agents)
        entities = []
        for i in range(n_agents, n_agents + num):
            eid = 'Agent_%d' % i
            self.agents.append(eid)
            entities.append({'eid': eid, 'type': model})

        return entities

    def step(self, time, inputs, max_advance):

        # print('%s - %s' % (time, inputs))

        self.time = time
        cache = self.cache = {}
        for agent_eid, attrs in inputs.items():
            values = attrs['val_in']
            assert len(values) == 1
            val_in = list(values.values())[0]

            if val_in > 1.1:
                cache[agent_eid] = 1.1/val_in - 0.1

        return None

    def get_data(self, outputs):
        data = {}
        for eid, attrs in outputs.items():
            if eid not in self.agents:
                raise ValueError('Unknown entity ID "%s"' % eid)

            data[eid] = {}
            for attr in attrs:
                if attr != 'mod':
                    raise ValueError('Unknown output attribute "%s"' % attr)
                if eid in self.cache:
                    data[eid][attr] = self.cache[eid]

        if data and self.output_delay:
            data['time'] = self.time + self.output_delay

        #print(data)

        return data


def main():
    return mosaik_api.start_simulation(Controller())


if __name__ == '__main__':
    main()
